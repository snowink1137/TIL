// function listUsers() {
//     setTimeout(() => {
//         const users = [
//             { id:1, githubID: '지상현'},
//             { id:2, githubID: 'jiss'},
//         ];
//         return users;
//     }, 2000)
// }


function getUser(id, callback) {
    setTimeout(() => {
        const users = [
            { id:1, githubID: '지상현'},
            { id:2, githubID: 'jiss'},
        ];
        const user = users.find(user => user.id ===id);
        console.log('Data Loaded!');
        console.log(user);
        callback(user);
    }, 2000)
}

const getRepos = (user, callback) => {
  setTimeout(() => {
      const repos = [
          'TIL', 'Workshop_HW', 'Python', 'JS'
      ];
      console.log('Data Loaded!');
      console.log(repos);
      callback(repos)
  }, 2000)
};

function getCommits (repo, callback) {
    setTimeout(()=>{
        const commits = [
            'Init repo',
            'Make index.html',
            'hahahah'
        ];
        console.log('Data Loaded!');
        console.log(commits);
        callback(commits);
    }, 2000)
}

// console.log('Start Program');
// getUser(1, user => {
//     console.log(user);
//     console.log('End Of Program');
// });

getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(`${commits.length} 개 커밋을 했네요!`)
        })
    })
});

// const user = {id:1,githubID:'지상현'};
//
// getRepos(user, (repos)=> {
//     console.log(repos)
// });




