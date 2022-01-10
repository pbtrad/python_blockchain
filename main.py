import hashlib

class PbtradCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Paul sends 5 PBC to Tiarnan"
t2 = "Tiarnan sends 3.3 PBC to Conor"
t3 = "Conor sends 4.6 PBC to Christine"
t4 = "Christine sends 1.2 PBC to Paul"

block1 = PbtradCoinBlock('genesisblock', [t1, t2])

print(f"block 1 data: {block1.block_data}")
print(f"block 1 data: {block1.block_hash}")

block2 = PbtradCoinBlock(block1.block_hash, [t3, t4])

print(f"Block 2 data: {block2.block_data}")
print(f"Block 2 hash: {block2.block_hash}")