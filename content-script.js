try {
  const outerDivs = document.querySelectorAll('.s-product-image-container');
  console.log("outerDivs.length有多少个：" + outerDivs.length);
  if (outerDivs) {
    const jsonData = {};
    //Math.min(outerDivs.length, 20)
    for (let i = 0; i < outerDivs.length; i++) {
      const outerDiv = outerDivs[i];
      const imageElements = outerDiv.querySelectorAll('img');
      if (imageElements.length > 0) {
        const newDiv = document.createElement('div');
        newDiv.classList.add('mytt666-custom-images'); // 可选：为新的 div 元素添加自定义类名
        newDiv.style.display = 'flex';

        const parentContainer = document.createElement('div');
        parentContainer.style.display = 'flex';
        parentContainer.style.flex = '1'; // 填充剩余空间

        var imageUrl = imageElements[0].src;
        var modifiedImageUrl = imageUrl.replace('_AC_UL320_.', '');;//得到am清晰地址图片
        var encodedUrlParam = encodeURIComponent(modifiedImageUrl);
        var url = 'http://localhost:5000/geturl?url=' + encodedUrlParam;
        
        fetch(url)
          .then(response => response.json())
          .then(jsonData => {
            for (let item of jsonData.items) {
              const { img, price, title, decoded_url } = item;

              const itemDiv = document.createElement('div');
              itemDiv.className = 'item';
              itemDiv.style.flex = '1';

              const linkElement = document.createElement('a');
              linkElement.href = decoded_url;
              linkElement.target = '_blank';

              const imgElement = document.createElement('img');
              imgElement.src = img;
              linkElement.appendChild(imgElement);
              itemDiv.appendChild(linkElement);

              const infoDiv = document.createElement('div');
              infoDiv.className = 'info';

              const titleElement = document.createElement('div');
              titleElement.className = 'title';
              titleElement.textContent = title.length > 9 ? title.substring(0, 9) + '..' : title;
              infoDiv.appendChild(titleElement);

              const priceElement = document.createElement('div');
              priceElement.className = 'price';
              priceElement.textContent = price;
              infoDiv.appendChild(priceElement);
              itemDiv.appendChild(infoDiv);

              parentContainer.appendChild(itemDiv);
              outerDiv.appendChild(parentContainer);
            }
          })
          .catch(error => {
            console.log('F_error：'+error);
          });

      } else {
        console.log("没找到图片");
      }
    }
  } else {
    console.log("没有找到元素。。");
  }
} catch (error) {
  console.error("Try_error:", error);
}