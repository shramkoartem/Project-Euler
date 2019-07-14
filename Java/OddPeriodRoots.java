// Problem 64

import java.lang.Math;

class OddPeriodRoots {

    public int getPeriodLength(int x) {

        int root = (int) Math.sqrt(x);

        if (root * root == x) {
            return 0;
        }

        //integer part of sqrt(x)
        int a = root;
        int nom = 0;

        int denom = 1;

        int period = 0;

        while (a != 2 * root) {
            nom = denom * a - nom;
            denom = (x - nom * nom) / denom;
            a = ((root + nom) / denom);

            period +=1 ;

        }


        return period;
    }

    public static void main(String[] args) {
        OddPeriodRoots s = new OddPeriodRoots();

        int count = 0;

        for (int i = 2; i < 10000; i++) {

            int ans = s.getPeriodLength(i);
            if (ans % 2 != 0) {
                count +=1;
            }

        }
        System.out.println(count);
    }
}
