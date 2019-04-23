function concat(str1, str2) {
    return `${str1} - ${str2}`;
}

const check_long_str = function (string) {
    if (string.length > 10) {
        return true;
    } else {
        return false;
    }
};

if (check_long_str(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING');
} else {
    console.log('SHORT STRING');
}

(check_long_str(concat('Happy', 'Hacking'))) ? console.log('LONG STRING') : console.log('SHORT STRING');