
// // import org.junit.jupiter.api.Assertions;
// // import org.junit.jupiter.api.DisplayName;
// // import org.junit.jupiter.api.Test;

// // class CalculatorTest {
// //     @Test
// //     @DisplayName("Loop test - multiplication of multiple inputs")
// //     public void testMultiplyWithLoop() {
// //         Calculator math = new Calculator();
// //         int[] firstInputs = {2, 3, 4, 5, -2};
// //         int[] secondInputs = {3, 4, 5, 6, 3};
// //         int[] expectedProducts = {6, 12, 20, 30, -6};
// //         for (int i = 0; i < firstInputs.length; i++) {
// //             int actual = math.multiply(
// //                 firstInputs[i],
// //                 secondInputs[i]
// //             );
// //             System.out.println(
// //                 "multiply(" + firstInputs[i] + ", "
// //                 + secondInputs[i] + ")"
// //             );
// //             Assertions.assertEquals(expectedProducts[i], actual);
// //         }
// //     }
// // }



// // import org.junit.jupiter.params.ParameterizedTest;
// // import org.junit.jupiter.params.provider.CsvSource;
// // import org.junit.jupiter.api.Assertions;
// // import org.junit.jupiter.api.DisplayName;

// // class CalculatorTest {
// //     @ParameterizedTest(name = "subtract({0}, {1}) should be {2}")
// //     @CsvSource({
// //         "9, 4, 5",
// //         "5, 8, -3",
// //         "7, 7, 0",
// //         "-4, -6, 2",
// //         "0, 5, -5"
// //     })
// //     @DisplayName("Parameterized subtraction test")
// //     public void testSubtractWithMultipleInputs(
// //             int a, int b, int expected) {
// //         Calculator math = new Calculator();
// //         int actual = math.subtract(a, b);
// //         System.out.println(
// //             "subtract(" + a + ", " + b + ") = " + actual
// //         );

// //         Assertions.assertEquals(expected, actual);
// //     }
// // }

// import org.junit.jupiter.api.Assertions;
// import org.junit.jupiter.api.Test;
// import org.junit.jupiter.api.DisplayName;
// import org.junit.jupiter.params.ParameterizedTest;
// import org.junit.jupiter.params.provider.CsvSource;

// class CalculatorTest {
//     @Test
//     @DisplayName("Test supported and unsupported operation names")
//     public void testOperationName() {

//         Calculator math = new Calculator();

//         Assertions.assertEquals(
//             "Addition",
//             math.operationName("+")
//         );

//         Assertions.assertNull(
//             math.operationName("%")
//         );
//     }

// }
