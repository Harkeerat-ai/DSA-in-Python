'''
L2-BinarySearchTreesTraversalsBalancings

This module provides two sets of utilities used for small demos and
manual testing:

- A minimal `user` model and a `UserDatabase` that supports inserting,
    finding, updating, and listing users. The database handles duplicate
    usernames, `None`/invalid inputs, and supports an optional case-sensitivity
    mode.

- A tiny binary-tree utility that can build a `TreeNode` structure from a
    nested-tuple representation (`build_tree`) and convert a tree back to the
    same nested-tuple format (`tree_to_tuple`). `build_tree` emits a debug
    print for each call to aid tracing recursive construction; `tree_to_tuple`
    returns scalar values for leaves so the reconstructed tuple matches the
    original mixed representation.

Public API / behavior summary:
- `user`: data holder with `username`, `name`, `email`, and `introduce()`.
- `UserDatabase`: `insert_user(user_obj)`, `find_user(username)`,
    `update(username, new_email)`, `list_all_users()` — returns clear
    messages useful for scenario testing.
- `TreeNode`, `build_tree(tup)`, `tree_to_tuple(node)` — helpers for
    converting between nested tuples and tree nodes.

The `if __name__ == "__main__"` block contains scenario tests demonstrating
Insert / Find / Update / List cases for the user database and verifies that
`tree_to_tuple(build_tree(orig_tuple)) == orig_tuple` for the provided example.
'''

class user:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce(self):
        return f"Username: {self.username}, Name: {self.name}, Email: {self.email}"

    def __repr__(self):
        return f"user(username={self.username!r}, name={self.name!r}, email={self.email!r})"


class UserDatabase:
    def __init__(self, case_sensitive: bool = True):
        # store users keyed by username (respecting case sensitivity flag)
        self._users = {}
        self.case_sensitive = case_sensitive

    def _key(self, username):
        if username is None:
            return None
        return username if self.case_sensitive else username.lower()

    def insert_user(self, user_obj):
        # validate user_obj
        if user_obj is None:
            return "Invalid user: None provided"
        if not hasattr(user_obj, 'username') or user_obj.username is None:
            return "Invalid user: username cannot be None"
        key = self._key(user_obj.username)
        if key in self._users:
            return f"Insert failed: username '{user_obj.username}' already exists"
        self._users[key] = user_obj
        return f"User {user_obj.username} inserted into database successfully"

    def find_user(self, username):
        if username is None:
            return "User not found"
        key = self._key(username)
        u = self._users.get(key)
        return u.introduce() if u is not None else "User not found"

    def update(self, username, new_email):
        if username is None:
            return "User not found"
        key = self._key(username)
        u = self._users.get(key)
        if u is None:
            return "User not found"
        u.email = new_email
        return f"User {u.username} email updated to {new_email}"

    def list_all_users(self):
        # return introduces in insertion order (dict preserves insertion order)
        return [u.introduce() for u in self._users.values()]

class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


if __name__ == "__main__":
    # Scenario tests requested by user
    db = UserDatabase(case_sensitive=True)

    print("\n--- Insert Scenarios ---")
    # 1. Insert into empty database
    aakash = user("aakash123", "Aakash", "aakash@example.com")
    print("Insert into empty DB:", db.insert_user(aakash))

    # 2. Try insert duplicate username
    duplicate = user("aakash123", "Aakash2", "aakash2@example.com")
    print("Insert duplicate username:", db.insert_user(duplicate))

    # 3. Insert username that does not exist
    biraj = user("biraj456", "Biraj", "biraj@example.com")
    print("Insert new username:", db.insert_user(biraj))

    # 4. Insert multiple users sequentially
    hemnath = user("hemnath789", "Hemnath", "hemnath@example.com")
    jadhesh = user("jadhesh012", "Jadhesh", "jadhesh@example.com")
    print(db.insert_user(hemnath))
    print(db.insert_user(jadhesh))

    # 5. Insert user with None username
    invalid = user(None, "NoName", "no@example.com")
    print("Insert user with None username:", db.insert_user(invalid))

    print("\n--- Find User Scenarios ---")
    # 1. Finding a user that exists
    print("Find existing (aakash123):", db.find_user("aakash123"))

    # 2. Searching for username that doesn't exist
    print("Find non-existent (unknown):", db.find_user("unknown"))

    # 3. Finding user after multiple inserts
    print("Find after multiple inserts (biraj456):", db.find_user("biraj456"))

    # 4. Case sensitivity test
    db_cs = UserDatabase(case_sensitive=True)
    db_cs.insert_user(user("User1", "U1", "u1@example.com"))
    print("Case-sensitive find 'User1':", db_cs.find_user("User1"))
    print("Case-sensitive find 'user1':", db_cs.find_user("user1"))

    print("\n--- Update Email Scenarios ---")
    # 1. Update existing
    print(db.update("aakash123", "aakash@new.com"))

    # 2. Attempt update for non-existent username
    print(db.update("noone", "noone@nowhere.com"))

    # 3. Update multiple times for same user
    print(db.update("aakash123", "aakash@v2.com"))
    print(db.update("aakash123", "aakash@v3.com"))

    # 4. Update right after insert
    temp = user("tempuser", "Temp", "temp@old.com")
    print(db.insert_user(temp))
    print(db.update("tempuser", "temp@new.com"))

    print("\n--- List All Users Scenarios ---")
    # Listing from empty database
    empty_db = UserDatabase()
    print("List from empty DB:", empty_db.list_all_users())

    # Listing after inserting single user
    single_db = UserDatabase()
    single_db.insert_user(user("single", "Single", "single@example.com"))
    print("List after single insert:", single_db.list_all_users())

    # Listing after multiple sequential inserts
    multi_db = UserDatabase()
    multi_db.insert_user(user("u1", "U1", "u1@example.com"))
    multi_db.insert_user(user("u2", "U2", "u2@example.com"))
    print("List after multiple inserts:", multi_db.list_all_users())

    # Calling list_all_users before any inserts vs after
    vdb = UserDatabase()
    print("Before inserts:", vdb.list_all_users())
    vdb.insert_user(user("last", "Last", "last@example.com"))
    print("After insert:", vdb.list_all_users())

    # Lets create objects representing each node of the tree
    tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

    # Function to build tree from nested tuple
    def build_tree(tup):
        print(f"build_tree called with: {tup!r}")
        if isinstance(tup, tuple) and len(tup) == 3:
            node = TreeNode(tup[1])
            node.left = build_tree(tup[0])
            node.right = build_tree(tup[2])
        elif tup is None:
            node = None
        else:
            node = TreeNode(tup)
        return node
    def tree_to_tuple(node):
        if node is None:
            return None
        # If it's a leaf, return the scalar key to match the original tuple format
        if node.left is None and node.right is None:
            return node.key
        left = tree_to_tuple(node.left)
        right = tree_to_tuple(node.right)
        return (left, node.key, right)
    def display_keys(node, space="\t", level=0):
        # If node is empty
        if node is None:
            print(space * level + "*")
            return
        # If node is leaf
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
        # If node has children 
        display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        display_keys(node.left, space, level + 1)

    root = build_tree(tree_tuple)
    # Display the constructed tree using tree_to_tuple and compare with original
    reconstructed = tree_to_tuple(root)
    print("Constructed tree as nested tuple:", reconstructed)
    print("Original tuple:", tree_tuple)
    if reconstructed == tree_tuple:
        print("tree_to_tuple returned a structure equal to the original tuple.")
    else:
        print("Warning: reconstructed tuple differs from original.")
    # Using display_keys to visualize the tree
    print("\nVisual representation of the tree:")
    display_keys(root,' ')