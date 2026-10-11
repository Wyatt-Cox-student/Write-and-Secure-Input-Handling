package partB;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

// The Incorrect Regex: https?://.+
// The original regex allows any character after http:// or https://, including spaces. 
// Because .+ matches almost anything, the program could capture text that isn't part of the URL.
// The suggested regex, https?://\S+, 
// works better because \S matches characters that are not whitespace. 
// This prevents the match from continuing through spaces, although it does not fully validate a URL.
public class urlValidation {
    public static void main(String[] args) {
        String text = "Visit my website at http://www.example.com";

        String regex = "https?://\\S+";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);

        while (matcher.find()) {
            System.out.println("URL: " + matcher.group());
        }
    }
}
// Replacing .+ with \\S+ prevents the regex from including spaces and unrelated words after the URL.
// It makes URL extraction more accurate, 
// although additional checks would be needed for complete URL validation.