from typing import List, Callable, Optional

from networkx import DiGraph


class MerkleNode:

    def __init__(self, right: int, left: Optional[int], entry: int) -> None:
        self.right = right
        self.left = left
        self.entry = entry

    def __str__(self) -> str:
        if self.right is None:
            return f"{self.entry}"
        h_entry = ""
        if self.left is not None:
            h_entry = f"{self.right} + {self.left}"
        else:
            h_entry = f"{self.right}"
        templ = f"h({h_entry}) = {self.entry}"


def compute_merkle_tree(merkle_list, transactions) -> DiGraph:
    """
    Compute the Merkle tree of a list of transactions
    """
    # TODO: Implement the Merkle tree
    # Create the Merkle tree
    merkle_tree = DiGraph()
    for i in reversed(range(len(merkle_list, -1))):
        merkle_layer = merkle_list[i]
        for j, merkle_entry in enumerate(merkle_layer):
            if i != 0:
                node = MerkleNode(right=merkle_list[i - 1][j*2], left=merkle_list[i - 1][j*2 + 1], entry=merkle_entry)
            
    return merkle_tree


def compute_merkle_list(transactions: List[int], hash_func: Callable[[int], int], operator_func = lambda a,b: a+b) -> List[List[int]]:
    """
    Compute the Merkle list of a list of transactions
    """
    # Create the list of Merkle nodes
    merkle_list = [[hash_func(transaction) for transaction in transactions]]

    while len(merkle_list[-1]) > 1:
        # Create the new list of Merkle nodes
        new_merkle_list = []
        for i in range(0, len(merkle_list[-1]), 2):
            if i + 1 < len(merkle_list[-1]):
                new_merkle_list.append(hash_func(operator_func(merkle_list[-1][i], merkle_list[-1][i + 1])))
            else:
                new_merkle_list.append(merkle_list[-1][i])
        merkle_list.append(new_merkle_list)
    return merkle_list