# Simple Blockchain Simulation

## Objective
This project is a basic blockchain simulation that demonstrates fundamental blockchain concepts such as block creation, hashing, proof-of-work, chain validation, and tamper detection.

## Features
✅ Blockchain with linked blocks  
✅ SHA-256 hashing for security  
✅ Proof-of-Work (difficulty-based mining)  
✅ Chain validation to prevent tampering  
✅ Demonstration of tampering detection  

## Assignment Requirements Fulfilled
- **Block Structure:** Each block contains an index, timestamp, transactions, previous hash, and current hash.
- **Hashing:** SHA-256 algorithm is used for secure hashing.
- **Blockchain Class:** Manages block creation and chain validation.
- **Proof-of-Work:** Implemented to make block mining computationally intensive.
- **Output Display:** Prints blockchain details and detects tampering.

## Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation
1. **Clone the repository**
   ```sh
   git clone <your-repository-URL>
   cd Simple-Blockchain
   ```
2. **Run the Python script**
   ```sh
   python blockchain.py
   ```

## How It Works
1. The blockchain starts with a **Genesis Block** (the first block in the chain).
2. New blocks can be added with **dummy transactions**.
3. Each block contains:
   - Index
   - Timestamp
   - Transactions
   - Hash of the previous block
   - Unique hash (generated using SHA-256)
   - Proof-of-Work (mining difficulty enforced)
4. If someone **modifies a block**, the blockchain detects it as invalid.

## Example Output
```
Index: 0
Timestamp: Mon Feb 10 12:00:00 2025
Transactions: ['Genesis Block']
Previous Hash: 0
Hash: 000abc123...
Nonce: 34567

Index: 1
Timestamp: Mon Feb 10 12:01:00 2025
Transactions: ['Alice pays Bob 5 BTC']
Previous Hash: 000abc123...
Hash: 000def456...
Nonce: 56789
```

## Tampering Demonstration
The script includes a function to modify a block’s transactions to simulate hacking. If a block is modified, the chain validation will fail:
```sh
Tampering with blockchain...
Is blockchain valid? False
```

## Submission Guidelines
- **GitHub Repository:** Ensure the project is available on a public or private GitHub repository.
- **README.md File:** Includes setup and execution instructions, project overview, and expected output.
- **Code Quality:** Properly commented, structured, and follows best practices.

## Author
**Devansh Sharma**



