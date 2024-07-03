public class first {
    //Write a Java program that prints the prime numbers among the integers numbers given
    //as command-line parameters.
    public static boolean isPrime(int n) {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n%2 == 0 || n%3 == 0)
            return false;
        for (int i = 5; i * i <= n; i += 6)
            if (n%i == 0 || n%(i + 2) == 0)
                return false;
        return true;
    }

    //read a number from terminal function
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

    public static void main(String[] args) throws Exception {
        int n = readInt();
        args = new String[n];
        for (int i = 0; i < n; i++)
            args[i] = Integer.toString(readInt());
        for (int i = 0; i < args.length; i++)
            if (isPrime(Integer.parseInt(args[i])))
                System.out.println(args[i] + " is prime");
            else
                System.out.println(args[i] + " is not prime");
    }
}