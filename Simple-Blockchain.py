import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, difficulty=2):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()
    
    def compute_hash(self):
        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()
    
    def mine_block(self):
        while True:
            self.hash = self.compute_hash()
            if self.hash[:self.difficulty] == '0' * self.difficulty:
                return self.hash
            self.nonce += 1

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, "0", ["Genesis Block"], self.difficulty)
        self.chain.append(genesis_block)
    
    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions, self.difficulty)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    
    def tamper_with_block(self, index, new_transactions):
        if 0 < index < len(self.chain):
            self.chain[index].transactions = new_transactions
            self.chain[index].hash = self.chain[index].compute_hash()

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}\n")

# Simulation
difficulty = 3
blockchain = Blockchain(difficulty)
blockchain.add_block(["Alice pays Bob 5 BTC"])
blockchain.add_block(["Bob pays Charlie 3 BTC"])
blockchain.display_chain()

# Tamper with blockchain
print("\nTampering with blockchain...")
blockchain.tamper_with_block(1, ["Alice pays Bob 100 BTC"])
blockchain.display_chain()

# Check validity
print("\nIs blockchain valid?", blockchain.is_chain_valid())
