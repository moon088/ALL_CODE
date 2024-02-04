	// windowにDOMContentLoadedの処理を登録
	window.addEventListener('DOMContentLoaded', e => {
		// ボタンの要素
		const elEf1 = document.querySelector('#ef1');
		const elEfBack = document.querySelector('#efBack');
		const elEfSave = document.querySelector('#efSave');
		const elEfDel = document.querySelector('#efDel');

		// Canvas関係の要素
		const canvas = document.querySelector('#view');
		const context = canvas.getContext('2d');

		//--------------------
		// セピアボタンをクリックしたときの処理
		elEf1.addEventListener('click', e => {
			// 読み込み日時の確認
			if (! checkTime()) { return; }

			// セピア色化
			efSepia(canvas, context);
		});

		// 戻すボタンをクリックしたときの処理
		elEfBack.addEventListener('click', e => {
			// 読み込み日時の確認
			if (! checkTime()) { return; }

			// 戻す
			efBack(context);
		});

		// 保存ボタンをクリックしたときの処理
		elEfSave.addEventListener('click', e => {
			// 読み込み日時の確認
			if (! checkTime()) { return; }

			// 保存
			efSave(canvas);
		});

		// 削除ボタンをクリックの処理
		elEfDel.addEventListener('click', e => {
			// 表示の変更
			const elNoView = document.querySelector('#noView');
			elNoView.style.display = 'block';
			canvas.style.display = 'none';

			// コメントの削除
			const elCmnt = document.querySelector('#comment');
			elCmnt.value = '';

			// ストレージを削除
			removeStorageCanvas();   // Canvas
			removeStorageComment();  // コメント

			// 初期値の復帰
			restoreStorageComment();  // コメント
		});

		//--------------------
		// 以降関数

		// 読み込み最終時刻
		let timeOld = null;
		let imgDataCache = null;

		// 読み込み日時の確認
		function checkTime() {
			// 読み込み日時の取得
			const time = canvas.getAttribute('time');

			// 読み込みがまだか確認
			if (time === null) { return false; }

			// 読み込みが新しいか確認
			if (time !== timeOld) {
				// ImageDataのキャッシュを得る
				imgDataCache = context.getImageData(
					0, 0, canvas.width, canvas.height);
			}

			// 読み込み日時の更新
			timeOld = time;

			// 正常終了という結果を戻す
			return true;
		}

		// セピア色化
		function efSepia(canvas, context) {
			// 変数の初期化
			const w = canvas.width;
			const h = canvas.height;
			const imgDt = context.getImageData(0, 0, w, h);
			const data = imgDt.data;

			// 画素に対して処理をする
			for (let i = 0; i < data.length; i += 4) {
				// RGBAを取り出す
				const r = data[i + 0];
				const g = data[i + 1];
				const b = data[i + 2];
				const a = data[i + 3];

				// 輝度を計算
				let Y = 0.298912 * r + 0.586611 * g + 0.114478 * b;
				Y = Math.trunc(Y);

				// RGBの値を上書き
				data[i + 0] = Math.trunc(Y * 240 / 255);
				data[i + 1] = Math.trunc(Y * 200 / 255);
				data[i + 2] = Math.trunc(Y * 145 / 255);
			}

			// ImageDataオブジェクトを描画する
			context.putImageData(imgDt, 0, 0);
		}

		// 戻す
		function efBack(context) {
			// ImageDataオブジェクトを描画する
			context.putImageData(imgDataCache, 0, 0);
		}

		// 保存
		function efSave(canvas) {
			// 画像ファイルの保存
			saveImage(canvas);

			// テキストファイル（コメント）の保存
			saveComment();
		}

		// 画像ファイルの保存
		function saveImage(canvas) {
			// Data URLを取り出す
			const dtUrl = canvas.toDataURL();

			// a要素の作成
			const elA = document.createElement('a');

			// ダウンロード用のファイル名を指定
			elA.setAttribute('download', 'save.png');

			// URLを指定
			elA.setAttribute('href', dtUrl);

			// bodyに追加して、クリックして、取りのぞく
			document.body.appendChild(elA);
			elA.click();
			elA.remove();
		}

		// テキストファイル（コメント）の保存
		function saveComment() {
			// コメント部分保存用の文字列を読み取る
			const elCmnt = document.querySelector('#comment');
			const txt = 'comment:' + elCmnt.value;

			// blobを作り、Object URLを作る
			const blob = new Blob([txt], {type: 'text/plain'});
			const url = URL.createObjectURL(blob);

			// a要素の作成
			const elA = document.createElement('a');

			// ダウンロード用のファイル名を指定
			elA.setAttribute('download', 'save.txt');

			// URLを指定
			elA.setAttribute('href', url);

			// bodyに追加して、クリックして、取りのぞく
			document.body.appendChild(elA);
			elA.click();
			elA.remove();

			// Object URLを破棄する
			URL.revokeObjectURL(url);
		}
	});