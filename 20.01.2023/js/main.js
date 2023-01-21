// Given a mathematical expression as a string you must return the result as a number.
// Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.
// Need to support the following mathematical operators:
//    Multiplication *
//    Division / (as floating point division)
//    Addition +
//    Subtraction -
// Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.
// Need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
// An addition to this rule is that the minus sign (-) used for negating numbers and parentheses 
// will never be separated by whitespace.

/* Solution one */
export const calc = (expression) => {
    // remove spaces from the input string
    expression = expression.replace(/\s/g, '');

    const operators = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => a / b
    };

    function isOperator(char) {
        return char in operators;
    }

    function getPrecedence(char) {
        if (char === '+' || char === '-') {
            return 1;
        } else if (char === '*' || char === '/') {
            return 2;
        }

        return 0;
    }

    function infixToPostfix(expression) {
        const stack = [];
        let output = '';

        for (const char of expression) {

            if (!isNaN(char) || char === '.') {
                output += char;
            } else if (isOperator(char)) {
                while (stack.length > 0 &&
                    isOperator(stack[stack.length - 1]) &&
                    getPrecedence(char) <= getPrecedence(stack[stack.length - 1])) {
                    output += stack.pop();
                }
                stack.push(char);

            } else if (char === '(') {
                stack.push(char);
            } else if (char === ')') {

                while (stack.length > 0 && stack[stack.length - 1] !== '(') {
                    output += stack.pop();
                }

                stack.pop();
            }
        }

        while (stack.length > 0) {
            output += stack.pop();
        }

        return output;
    }

    function evaluatePostfix(expression) {
        const stack = [];

        for (const char of expression) {

            if (!isNaN(char) || char === '.') {
                stack.push(parseFloat(char));
            } else if (isOperator(char)) {
                const b = stack.pop();
                const a = stack.pop();
                const result = operators[char](a, b);
                stack.push(result);
            }
        }

        return stack.pop();
    }

    const postfix = infixToPostfix(expression);

    return evaluatePostfix(postfix);
}


// Write algorithm using javascript that accept in parameter a mathematical expression as a string and returns the result as a number.
// Numbers passed to the function may be both whole numbers and/or decimal numbers. Returned value also may be whole numbers and/or decimal numbers.
//  Need to support the following mathematical operators:
//     1. Multiplication *
//     2. Division / (as floating point division)
//     3. Addition +
//     4. Subtraction -
// Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.
// Need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
// Minus sign (-) used for negating numbers and parentheses will never be separated by whitespace.


// Test the last algorithm with these test cases. If one of them not equal to the value I put after == then fix algorithm until all test cases will be equal to the values I passed after symbol ==.
//     '1+1' == 2
//     '1 - 1' == 0
//     '1* 1' == 1
//     '1 /1' == 1
//     '-123' == -123
//     '123' == 123
//     '2 /2+3 * 4.75- -6' == 25
//     '12* 123' == 1476
//     '2 / (2 + 3) * 4.33 - -6' == 7.732