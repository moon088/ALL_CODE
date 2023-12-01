	// sumの読み込み
	const sum = require('./sum');

	// テストの実行
	test('adds 1 + 2 to equal 3', () => {
		expect(sum(1, 2)).toBe(3);
	});