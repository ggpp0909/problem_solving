import java.util.Scanner;

public class Main_1110 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int original = sc.nextInt();
        int changed = calculate(original);

        int ans = 1;
        while (original != changed) {
            changed = calculate(changed);
            ans ++;
        }
        System.out.println(ans);

    }

    public static int calculate(int num) {
        if (num < 10) {
            return num * 10 + num;
        }
        int A = num / 10;
        int B = num % 10;
        int C = (A + B) % 10;
        return  B * 10 + C;
    }
}
