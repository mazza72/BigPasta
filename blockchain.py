import requests, json, hashlib
from time import time
from urllib import parse


class Blockchain():
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.nodes = set()
        self.use_values = {}

        self.new_block(previous_hash=1, genesis=True)


    def new_block(self, previous_hash=None, genesis=False):
        if not previous_hash:
            previous_hash = self.hash(self.chain[-1])

        block = [{
                'index' : len(self.chain) + 1,
                'timestamp' : time(),
                'transactions' : self.pending_transactions,
                'previous_hash' : previous_hash
                }]
        print("Before the nodes")
        if genesis:
            self.chain.append(block)
        else:
            for i in self.nodes:
                print("Running in nodes")
                if i.lead_consensus(block):
                    print("It was true")
                    self.pending_transactions = []
                    self.chain.append(block)
                break



    def new_transaction(donationID, recipient, useID, amount):
        self.pending_transactions.append({
                'donationID': donationID,
                'recipient': recipient,
                'useID': useID,
                'amount': amount
                })
        return self.last_block['index'] + 1


    def register_node(self, address):
        parsed_url = parse.urlparse(address)
        self.nodes.add(parsed_url.netloc)


    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block():
        return self.chain[-1]


    def new_node(self, node_address):
        node_address = parse.urlparse(node_address)
        self.nodes.add(node_address)


    def lead_consensus(self, block_to_add):
        response_count_true = 0
        response_count_false = 0
        for node in self.nodes:
            # UPDATE TO USE REQUESTS MODULE ON NODE
            if node.add_consensus(block_to_add):
                response_count_true += 1
            else:
                response_count_false += 1

            if response_count_true > len(nodes) / 3:
                return True
            elif response_count_false > len(nodes) / 3:
                return False


    def add_consensus(self, check_block):
        for transaction in block['transactions']:
            use = transaction['useID']
            val = transaction['amount']
            if use in use_values:
                use_values += val
                if use_values < 0:
                    return False
                else:
                    return True


    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False

            last_block = block
            current_index += 1

        return True


    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None

        max_length = len(self.chain)

        for node in neighbours:
            response = requests.get(f"http://{node}/chain" )

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

test = Blockchain()
test.new_node("http://0.0.0.0:5000")
print("Initialised")
print(f"In the blockchain there is {test.chain}")
test.new_block()

# transaction_example = {
#     'index': 1,
#     'timestamp': 1506057125.900785, # Unix time
#     'transactions': [
#         {
#             'donationID': "8527147fe1f5426f9dd545de4b27ee00",
#             'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
#             'useID': "9274fabf5426dfa254a57147fe1"
#             'amount': 10.00,
#         }
#     ],
#     'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824" # Hash of the previous block.
# }
