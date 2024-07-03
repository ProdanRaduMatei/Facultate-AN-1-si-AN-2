public class second {
    //Write a Java program that prints the maximum value from all the double numbers given
    //as command-line parameters.

    public static int readInt() throws Exception {
        int n = 0;
        boolean negative = false;
        int c = System.in.read();
        while (c < '0' || c > '9') {
            if (c == '-')
                negative = true;
            c = System.in.read();
        }
        while (c >= '0' && c <= '9') {
            n = n * 10 + c - '0';
            c = System.in.read();
        }
        if (negative)
            n = -n;
        return n;
    }

    public static void main(String[] args) {
        int max = Integer.MIN_VALUE;
        //read the number of elements
        int n = readInt();
        
    }
}
