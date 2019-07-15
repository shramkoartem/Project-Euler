// Problem 65

import java.math.BigInteger;

public class ConvergentsOfE {

    public static long sumDigits(long i) {
        return i == 0 ? 0 : i % 10 + sumDigits(i / 10);
    }

    public static void main(String[] args){

        ConvergentsOfE e = new ConvergentsOfE();

        int limit = 100;
        int res = 0;

        BigInteger n0 = new BigInteger("1");
        BigInteger n1 = new BigInteger("2");

        for (int i=2; i <= limit; i++){
            BigInteger temp = n1;
            int c = (i%3==0) ?  2*(i/ 3) : 1;
            n1 = n0.add( n1.multiply(BigInteger.valueOf(c)) );
            n0 = temp;
            System.out.println(n1);

        }

        System.out.println(n1);

        String digits = n1.toString();
        int sum = 0;

        for(int i = 0; i < digits.length(); i++) {
            int digit = (int) (digits.charAt(i) - '0');
            sum = sum + digit;
        }

        System.out.println(sum);
