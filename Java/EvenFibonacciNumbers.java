// Problem 002

public class EvenFibonacciNumbers {
    public static void main(String[] args){
        int a = 1;
        int b = 2;
        //sum
        int s = 2;

        while(b < 4000000){
            int c = a+b;
            a = b;
            b = c;

            if(b%2==0){
                s += b;
            }
        }
        System.out.println(s);
    }
}
