	// 待機用の関数
	function p(tm, isResolve = true) {
		// Promiseオブジェクトを戻り値にする
		return new Promise((resolve, reject) => {
			// tmミリ秒待って実行
			setTimeout(() => {
				// コンソールに情報を出力
				console.log(tm, isResolve ? 'resolve' : 'reject');

				if (isResolve) {
					// isResolveがtrueなら解決
					resolve(`${tm}:ok`);
				} else {
					// isResolveがfalseなら拒否
					reject(`${tm}:err`);
				}
			}, tm);
		});
	};