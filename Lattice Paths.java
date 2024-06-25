import java.math.BigInteger;
class GridRoutes {
    public static void main(String args[]) {
        BigInteger result = factorial(40).divide(factorial(20).multiply(factorial(20)));
        System.out.println("Number of routes: " + result);
    }

    public static BigInteger factorial(int n) {
        BigInteger fact = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }
}
