// Write a function that when given a URL as a string,
// parses out just the domain name and returns it as a string


/* Solution one */
export const domainName = (url) => {
    const regex = /^(?:https?:\/\/)?(?:www\.)?([^./]+)\./i;
    const match = url.match(regex);

    return match ? match[1] : '';
}
