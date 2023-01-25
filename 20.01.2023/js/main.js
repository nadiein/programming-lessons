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

// Steps:
// 1. Check if there is only one digit in expression then return value
// 2. Remove from the string spaces
// 3. Define math operations

/* Solution one */
export const calc = (expression) => {
    // remove spaces from the input string
    expression = expression.replace(/\s/g, '');

    if (expression.match(/^-?[0-9]+?$/g)) return Number(expression);

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
