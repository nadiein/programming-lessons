// Write a function which formats a duration, given as a number of seconds, in a human-friendly way.
// The function must accept a non-negative integer. If it is zero, it just returns "now".
// Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.


/* Solution one */
export const formatDuration = (seconds) => {
    if (seconds === 0) return 'now';

    const units = [
        {value: 31536000, name: 'year'},
        {value: 86400, name: 'day'},
        {value: 3600, name: 'hour'},
        {value: 60, name: 'minute'},
        {value: 1, name: 'second'},
    ];

    let result = '';

    for (let i = 0; i < units.length; i++) {
        if (seconds >= units[i].value) {
            let count = Math.floor(seconds / units[i].value);

            seconds = seconds % units[i].value;
            result += `${count} ${units[i].name}` + (count > 1 ? 's' : '') + ', ';
        }
    }

    return result.slice(0, -2).replace(/,([^,]*)$/, ' and$1');
}
