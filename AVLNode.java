public class AVLNode {
  public AVLNode left = null;
  public AVLNode right = null;
  public int value = 0;
  public AVLNode parent = null;

  public AVLNode insert(int newValue) {
    // perform binary-search style insertion
    if (newValue < this.value) {
      // insert the value to the left sub-tree
      if (this.left == null) {
        AVLNode newNode = new AVLNode();
        newNode.value = newValue;
        newNode.parent = this;
        this.left = newNode;
      } else {
        this.left.insert(newValue);
      }
    } else {
      // insert the value into the right sub-tree
      if (this.right == null) {
        AVLNode newNode = new AVLNode();
        newNode.value = newValue;
        newNode.parent = this;
        this.right = newNode;
      } else {
        this.right.insert(newValue);
      }
    }

    return rebalance();
  }

  public AVLNode rebalance() {
    // balance the tree (if necessary)
	  AVLNode orphan = new AVLNode();
	  AVLNode root = this;
	  if (root.getBalance() > 1)
	  {
		  if (root.left.getBalance() == -1)
		  {
			  orphan = root.left.right;
			  root = root.left;
			  root.right = root;
			  root.left = orphan;
			 // Single right rotation
		  }
		  orphan = root.right.left;
		  root = root.right;
		  root.left = root;
		  root.right = orphan;
		  // Single left rotation  
	  }
	  
	  if (root.getBalance() < -1)
	  {
		  System.out.println("test1");
		  if (root.right.getBalance() == 1)
		  {
			  System.out.println("test2");
			  orphan = root.right.left;
			  root = root.right;
			  root.left = root;
			  root.right = orphan;
			 // Single left rotation 
		  }
		  
		  orphan = root.left.right;
		  root = root.left;
		  root.right = root;
		  root.left = orphan;
		  // Single right rotation   
	  }
    return null;
    
  }

  public int getBalance() {
    int rightHeight = 0;
    if (this.right != null) {
      rightHeight = this.right.getHeight();
    }

    int leftHeight = 0;
    if (this.left != null) {
      leftHeight = this.left.getHeight();
    }

    return rightHeight - leftHeight;
  }

  public void print(int depth) {
    if (this.right != null) {
      this.right.print(depth + 1);
    }

    for (int i = 0; i < depth; i++) {
      System.out.print("\t");
    }
    System.out.println(this.value);

    if (this.left != null) {
      this.left.print(depth + 1);
    }
  }

  public int getHeight() {
    int leftHeight = 1;
    if (left != null) {
      leftHeight = left.getHeight() + 1;
    }

    int rightHeight = 0;
    if (right != null) {
      rightHeight = right.getHeight() + 1;
    }

    return (leftHeight > rightHeight) ? leftHeight : rightHeight;
  }
}
