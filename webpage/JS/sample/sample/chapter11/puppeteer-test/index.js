	// モジュールの読み込み
	const puppeteer = require('puppeteer-core');

	// Google Chromeのパスを作成
	const chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe';

	// URL
	const url = 'https://github.com/puppeteer/puppeteer';

	// ヘッドレスの状態（真偽値で状態を切りかえ）
	const isHeadless = true;

	// Puppeteer実行用関数
	async function exec() {
		// Webブラウザの起動
		// デフォルトでは、800x600のサイズで画面を作る
		const browser = await puppeteer.launch({
			executablePath: chrome,
			headless: isHeadless,  // デフォルトはtrueで画面が出ない
			slowMo: 500  // 操作を500ミリ秒に落とす
		});

		// 新しいページを開く
		const page = await browser.newPage();

		// URLに移動
		await page.goto(url);

		// PDF出力
		// ヘッドレスのときだけ使える機能
		if (isHeadless) {
			await page.pdf({path: 'html.pdf', format: 'A4'});
		}

		// コンソールの出力内容を取得して表示する
		page.on('console', msg => console.log('PAGE LOG:', msg.text()));

		// コードの実行
		await page.evaluate(() => {
			// コンソールに情報を出力
			console.log(`url is ${location.href}`);
		});

		// コードの実行
		await page.evaluate(() => {
			// 最初のhttpsではじまるリンクをクリック
			Array.from(document.querySelectorAll('a'))
			.filter(x => x.getAttribute('href').match(/^https:/))
			[0].click();
		});

		// ブラウザを閉じる
		await browser.close()

		// コンソールに終了を通知
		console.log('end');
	}

	// Puppeteer実行
	exec();