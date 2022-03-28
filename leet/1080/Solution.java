class Solution {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }


    public static boolean isLeaf( TreeNode node ) {
        return node.left == null && node.right == null;
    }

    public static TreeNode depthFirst( TreeNode currentRoot, int currentSum, int limit ) {

        //region Edge Checking
        if ( currentRoot == null ) {
            return null;
        }
        //endregion


        // region Action
        int total = currentSum + currentRoot.val;
        if ( isLeaf( currentRoot ) ) {
            if ( total < limit ) {
                return null;
            }
            return currentRoot;
        }

        // endregion

        //region recurse
        currentRoot.left = depthFirst( currentRoot.left, total, limit );
        currentRoot.right = depthFirst( currentRoot.right, total, limit );

        if ( isLeaf( currentRoot ) ) {
            return null;
        }
        //endregion
        return currentRoot;
    }

    public TreeNode sufficientSubset( TreeNode root, int limit ) {
        return ssufficientSubset( root, limit );
    }

    public static TreeNode ssufficientSubset( TreeNode root, int limit ) {


        return depthFirst( root, 0, limit );

    }

    public static void main( String[] args ) {

    }
}

public class TreeNode {
    int      val;
    TreeNode left;
    TreeNode right;

    TreeNode( )         {}

    TreeNode( int val ) {this.val = val;}

    TreeNode( int val, TreeNode left, TreeNode right ) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
