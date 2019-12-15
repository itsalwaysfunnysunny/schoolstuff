public class AVLDriver {
  public static void add(AVLTree tree, int value) {
    tree.insert(value);
    System.out.printf("After insert %d:\n", value);
    tree.print();
    System.out.println("");
  }
  public static void main(String[] args) {
    AVLTree tree = new AVLTree();
    System.out.println("Initial:");
    tree.print();

    // double rotation right
    /*
    add(tree, 2);
    add(tree, 1);
    add(tree, 6);
    add(tree, 7);
    add(tree, 4);
    add(tree, 3);
    add(tree, 5);
    */

    // double rotation left:
    add(tree, 6);
    add(tree, 7);
    add(tree, 2);
    add(tree, 1);
    add(tree, 4);
    /*add(tree, 3);
    add(tree, 5);*/
  }
}
