// Write a function, which takes a non-negative integer (seconds)
// as input and returns the time in a human-readable format (HH:MM:SS)
// Constraints:
// HH = hours, padded to 2 digits, range: 00 - 99
// MM = minutes, padded to 2 digits, range: 00 - 59
// SS = seconds, padded to 2 digits, range: 00 - 59
// The maximum time never exceeds 359999 (99:59:59)

/* Solution one */
export const makeReadable = (seconds) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds - (h * 3600)) / 60);
    const s = seconds - (h * 3600) - (m * 60);

    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

makeReadable(0) /* "00:00:00" */
makeReadable(5) /* "00:00:05" */
makeReadable(60) /* "00:01:00" */
makeReadable(86399) /* "23:59:59" */
makeReadable(359999) /* "99:59:59" */