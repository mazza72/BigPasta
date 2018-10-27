import requests, json, hashlib


class Blockchain():
    def __init__():
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash=1, proof=100)


    def new_block(self, proof, previous_hash=None):
        if not previous_hash:
            previous_hash = self.hash(self.chain[-1])

        block = [{
                'index' : len(self.chain) + 1
                'timestamp' :
                'transactions' : self.pending_transactions
                'proof' : proof
                'previous_hash' : previous_hash
                }]

        self.pending_transactions = []
        self.chain.append(block)


    def new_transaction(donationID, recipient, amount):
        self.pending_transactions.append({
                'donationID': donationID,
                'recipient': recipient,
                'amount': amount
                })
        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block():
        return self.chain[-1]


# transaction_example = {
#     'index': 1,
#     'timestamp': 1506057125.900785, # Unix time
#     'transactions': [
#         {
#             'donationID': "8527147fe1f5426f9dd545de4b27ee00",
#             'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
#             'amount': 10.00,
#         }
#     ],
#     'proof': 324984774000,
#     'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824" # Hash of the previous block.
# }
