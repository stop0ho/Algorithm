// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	let N;
	let money = 0;
	
	for await (const line of rl) {
		if (!N) { N = line; }
		else {
			let [op, cnt] = line.split(' ');
			if (op === 'in') { money += Number(cnt) }
			else {
				if (money < Number(cnt)) {
					console.log('fail');
					process.exit();
				}
				money -= Number(cnt)}
		}
	}
	
	if (money < 0) console.log('fail');
	else console.log('success');
	
	process.exit();
})();
