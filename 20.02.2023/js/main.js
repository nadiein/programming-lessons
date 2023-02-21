// Algorithm strips all text that follows any of a set of comment markers passed in.
// Any whitespace at the end of the line should also be stripped out.
// Example:

// Given an input string of:
// apples, pears # and bananas
// grapes
// bananas !apples

// The output expected would be:
// apples, pears
// grapes
// bananas
// The code would be called like so:

// var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"


/* Solution one */
export const solution = (input, markers) => {
    // Split the input string into lines
    let lines = input.split('\n');

    // Loop through each line
    for (let i = 0; i < lines.length; i++) {
        let line = lines[i];

        // Find the first occurrence of any of the comment markers
        for (let j = 0; j < markers.length; j++) {
            let index = line.indexOf(markers[j]);

            if (index !== -1) {
                // Strip out the comment and any whitespace at the end of the line
                line = line.substring(0, index).trimRight();
                break;
            }
        }

        // Update the line in the array
        lines[i] = line;
    }

    // Join the lines back into a single string and return it
    return lines.join('\n');
}