
public class Calculator {

    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public int divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Cannot divide by zero");
        }
        return a / b;
    }

    public String operationName(String operator) {
        switch (operator) {
            case "+":
                return "Addition";
            case "-":
                return "Subtraction";
            case "*":
                return "Multiplication";
            case "/":
                return "Division";
            default:
                return null;
        }
    }
}
