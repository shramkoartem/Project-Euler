// Problem 4

class LargestPalindromeProduct {

    public LargestPalindromeProduct() {
    };

    public boolean palindrome(int n){
        String num = Integer.toString(n);

        int len = num.length();
        int forward = 0;
        int backward = len-1;
        while(backward > forward){
            char fChar = num.charAt(forward);
            char bChar = num.charAt(backward);
            if(fChar != bChar){
                return false;
            }
            forward += 1;
            backward -= 1;
        }
        return true;
    };



    public static void main(String[] args) {

        LargestPalindromeProduct s = new LargestPalindromeProduct();

        int m = 1;

        for(int i = 999; i > 900; i--){
            for(int j = 999; j > 900; j--){
                int a = i * j;
                if (s.palindrome(a)){
                    if (a > m) {
                        m = a;
                    }
                }
            }
        }

        System.out.println(m);
    }
}
