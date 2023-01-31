// Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
// Modern Roman numerals are written by expressing each digit separately starting with the left
// most digit and skipping any digit with a value of zero.
// In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
// 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.


/* Solution one */
export class RomanNumerals {

    static fromRoman = (str) => {
        const map = {
            I: 1,
            V: 5,
            X: 10,
            L: 50,
            C: 100,
            D: 500,
            M: 1000
        };

        let result = 0;

        for ( let i = 0; i < str.length; i++ ) {
            let current = map[str[i]];
            let next = map[str[i + 1]];

            if ( next > current ) {
                result += next - current;
                i++;
            } else {
                result += current;
            }
        }
        return result;
    }

    static toRoman = (num) => {
        const map = [
            { roman: 'M', value: 1000 },
            { roman: 'CM', value: 900 },
            { roman: 'D', value: 500 },
            { roman: 'CD', value: 400 },
            { roman: 'C', value: 100 },
            { roman: 'XC', value: 90 },
            { roman: 'L', value: 50 },
            { roman: 'XL', value: 40 },
            { roman: 'X', value: 10 },
            { roman: 'IX', value: 9 },
            { roman: 'V', value: 5 },
            { roman: 'IV', value: 4 },
            { roman: 'I', value: 1 }
        ];

        let result = '';

        for ( const { roman, value } of map ) {

            while ( num >= value ) {
                result += roman;
                num -= value;
            }
        }
        return result;
    }
}
