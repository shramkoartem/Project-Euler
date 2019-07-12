// Problem 003

import java.lang.Math;


public class LargestPrimeFactor {

    public static boolean prime(int n){
        boolean ans = true;

        int lim = (int) (Math.sqrt(n)+1);

        if(n%2==0 && n!=2){
            ans = false;
        }

        for(int i=3; i < lim; i += 2){
            if(n%i==0){
                ans = false;
            }
        }
        return(ans);
    }

    public static void main(String[] args){

        //BigInteger num = new BigInteger("600851475143");
        long num = 600851475143L;
        int maxPrime = 2;

        for(int i = 2; i < Math.sqrt(num)+1; i++)
            if (num%i == 0) {
                if (prime(i)) {
                    maxPrime = i;
                }
            }
        System.out.println(maxPrime);
    }
}
