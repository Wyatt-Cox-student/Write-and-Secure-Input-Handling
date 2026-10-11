package partB;

import java.util.Scanner;
import java.util.regex.Pattern;

// The Incorrect Regex: ^\\d{5}(\\d{4})?$
// The original regex checks for either five digits or nine digits without a separator. 
// However, the program asks the user to enter either xxxxx or xxxxx-xxxx. 
// The regex is missing the hyphen between the first five digits and the optional final four digits.
public class ZipCode {
    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {

            Pattern zipPattern =
                Pattern.compile("^[0-9]{5}(-[0-9]{4})?$");

            System.out.println(
                "Enter a Zipcode as xxxxx or xxxxx-xxxx: "
            );

            String zipCode = scanner.nextLine();

            if (!zipPattern.matcher(zipCode).matches()) {
                System.out.println("Incorrect Zipcode");
            }
            else {
                System.out.println("Correct Zip");
            }
        }
    }
}
// The corrected regex should accept exactly five digits or five digits followed by a hyphen 
// and four more digits. It rejects ZIP codes that do not match either requested format.
