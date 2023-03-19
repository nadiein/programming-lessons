// Function should convert passing in RGB decimal values in a hexadecimal representation


/* Solution one */
export const rgbOne = (r, g, b) => {
    // Round the input values to the nearest valid range [0, 255]
    r = Math.max(0, Math.min(255, Math.round(r)));
    g = Math.max(0, Math.min(255, Math.round(g)));
    b = Math.max(0, Math.min(255, Math.round(b)));

    // Convert the decimal values to their hexadecimal representation
    const hexR = r.toString(16).padStart(2, '0');
    const hexG = g.toString(16).padStart(2, '0');
    const hexB = b.toString(16).padStart(2, '0');

    // Concatenate the three hexadecimal values to form the final output
    return String(hexR + hexG + hexB).toUpperCase();
}

/* Solution two */
export const rgbTwo = (r, g, b) => {
    // Round the input values to the nearest valid range [0, 255]
    r = Math.max(0, Math.min(255, Math.round(r)));
    g = Math.max(0, Math.min(255, Math.round(g)));
    b = Math.max(0, Math.min(255, Math.round(b)));

    // Convert the decimal values to their hexadecimal representation
    const hexR = r.toString(16);
    const hexG = g.toString(16);
    const hexB = b.toString(16);

    // Pad each hexadecimal value with a leading zero if necessary
    const paddedR = hexR.length < 2 ? '0' + hexR : hexR;
    const paddedG = hexG.length < 2 ? '0' + hexG : hexG;
    const paddedB = hexB.length < 2 ? '0' + hexB : hexB;

    // Concatenate the three hexadecimal values to form the final output
    return String(paddedR + paddedG + paddedB).toUpperCase();
}

/* Solution three */
export const rgbThree = (r, g, b) => {
    // Round the input values to the nearest valid range [0, 255]
    r = Math.max(0, Math.min(255, Math.round(r)));
    g = Math.max(0, Math.min(255, Math.round(g)));
    b = Math.max(0, Math.min(255, Math.round(b)));

    // Convert the decimal values to their hexadecimal representation
    const hex = (r << 16) | (g << 8) | b;

    // Convert the hexadecimal value to a string and pad it with leading zeros if necessary
    return String(('000000' + hex.toString(16)).slice(-6)).toUpperCase();
}

/* Solution four */
export const rgbFour = (r, g, b) => {
    // Round the input values to the nearest valid range [0, 255]
    r = Math.max(0, Math.min(255, Math.round(r)));
    g = Math.max(0, Math.min(255, Math.round(g)));
    b = Math.max(0, Math.min(255, Math.round(b)));

    // Define a lookup table for hexadecimal digits
    const hexTable = '0123456789abcdef';

    // Convert each decimal value to its corresponding hexadecimal digit
    const hexR = hexTable[Math.floor(r / 16)] + hexTable[r % 16];
    const hexG = hexTable[Math.floor(g / 16)] + hexTable[g % 16];
    const hexB = hexTable[Math.floor(b / 16)] + hexTable[b % 16];

    // Concatenate the three hexadecimal values to form the final output
    return String(hexR + hexG + hexB).toUpperCase();
}

/* Solution five */
export const rgbFive = (r, g, b) => {
    // Round the input values to the nearest valid range [0, 255]
    r = Math.max(0, Math.min(255, Math.round(r)));
    g = Math.max(0, Math.min(255, Math.round(g)));
    b = Math.max(0, Math.min(255, Math.round(b)));

    // Convert the decimal values to their hexadecimal representation
    const hex = [r, g, b].map(x => x.toString(16).padStart(2, '0')).join('');

    // Use a regular expression to format the output as a six-digit hexadecimal number
    return String(hex.replace(/^([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/, '$1$2$3')).toUpperCase();
}
