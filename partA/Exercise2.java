package partA;
// The Incorrect Variable is: String y = 10;\
// The variable y is declared as a String, but it is assigned an integer. 
// Java does not automatically convert an integer into a String during this assignment, 
// so this causes a compilation error.
public class Exercise2 {
    public static void main(String[] args) {
        int y = 10;
        System.out.println("The value of y is: " + y);
    }
}
// Changing the variable type to int makes it match the value being stored. 
// This prevents the type mismatch error.