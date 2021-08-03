const getUser = id => {
    const users = [
        { id:1, githubID: '지상현'}, { id:2, githubID: 'jiss'},
    ];
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const user = users.find(user => user.id ===id);
            if (user) resolve(user);
            else reject(new Error(`Can't find user ${id}`));
        }, 2000)
    })
};

const getRepos = (user) => {
    const repos = [
        'TIL', 'Workshop_HW', 'Python', 'JS'
    ];
    return new Promise( (resolve, reject)=> {
        setTimeout(() => {
            if (repos) resolve(repos);
            else reject(new Error('No Repos'));
        }, 2000)
    })
};

const getCommits = repo => {
    const commits = ['Init repo', 'Make index.html', 'hahahah'];
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            if (commits) resolve(commits);
            else reject(new Error('ERRRRRRRRRRRRRRRORRRRR'));
        }, 2000)
    });
};

getUser(2)
    .then(user => getRepos(user))
    .then(repos => getCommits(repos[0]))
    .then(commits => console.log(commits.length))
    .catch(err => console.error(err));

// getUser(1, user => {
//     getRepos(user, repos => {
//         getCommits(repos[0], commits => {
//             console.log(`${commits.length} 개 커밋을 했네요!`)
//         })
//     })
// });