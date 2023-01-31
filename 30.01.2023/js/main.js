// In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
// Create as many "shufflings" as you can!


/* Solution one */
export const permutations = (string) => {
    const results = [];

    const generate = (input, chosen) => {

        if (!input) {
            results.push(chosen);
            return;
        }

        for (let i = 0; i < input.length; i++) {
            let remaining = input.substring(0, i) + input.substring(i + 1);
            generate(remaining, chosen + input[i]);
        }
    }

    generate(string, '');

    return [...new Set(results)];
}
