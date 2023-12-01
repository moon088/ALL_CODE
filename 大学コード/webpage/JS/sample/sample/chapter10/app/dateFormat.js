	// 日時フォーマット
	function dateFormat(txt, d) {
		// 引数dが未指定なら現在の時刻でDateオブジェクトを作成
		if (d === undefined) { d = new Date(); }

		// 桁揃え用の関数
		const dgt = (m, n) => `${m}`.padStart(n, '0').substr(-n);

		// 置換用の配列を作成
		const arr = [
			 {k: 'YYYY', v: d.getFullYear()}
			,{k: 'MM',   v: dgt(d.getMonth() + 1, 2)}
			,{k: 'DD',   v: dgt(d.getDate(), 2)}
			,{k: 'hh',   v: dgt(d.getHours(), 2)}
			,{k: 'mm',   v: dgt(d.getMinutes(), 2)}
			,{k: 'ss',   v: dgt(d.getSeconds(), 2)}
		];

		// 置換用の配列を使って、引数tの内容を置換する
		arr.forEach(x => txt = txt.replace(x.k, x.v));

		// 置換結果を戻す
		return txt;
	}