try {
  // 找到最外层的 div 元素
  const outerDivs = document.querySelectorAll('.s-product-image-container');
  console.log("outerDivs.length有多少个：" + outerDivs.length);

  // 如果找到了元素
  if (outerDivs) {
    // 创建一个对象来存储前十个图片地址
    const jsonData = {};

    // 遍历前13个外层div元素并获取其图片地址 Math.min(outerDivs.length, 2)
    for (let i = 0; i < outerDivs.length; i++) {
      const outerDiv = outerDivs[i];
      
      const imageElements = outerDiv.querySelectorAll('img');
      if (imageElements.length > 0) {

        // 创建一个新的 div 元素，用于容纳两张图片
        const newDiv = document.createElement('div');
        newDiv.classList.add('mytt666-custom-images'); // 可选：为新的 div 元素添加自定义类名
        newDiv.style.display = 'flex'; // 添加display:flex属性
        newDiv.style.width = '50%';

        // 创建存放itemDiv的父容器
        const parentContainer = document.createElement('div');
        parentContainer.style.display = 'flex'; // 添加display:flex属性
        parentContainer.style.flex = '1'; // 填充剩余空间

        var encodedUrlParam = encodeURIComponent(imageElements[0].src);
        var url = 'http://localhost:5000/geturl?url=' + encodedUrlParam;
        
        fetch(url)
          .then(response => response.json())
          .then(jsonData => {
            for (let item of jsonData.items) {
              const { img, price, title, decoded_url } = item;

              const itemDiv = document.createElement('div');
              itemDiv.className = 'item';
              itemDiv.style.flex = '1'; // 添加flex:1属性
              // itemDiv.style.marginRight = '0'; // 去除默认外边距

              const linkElement = document.createElement('a'); // 创建 <a> 标签
              linkElement.href = decoded_url; // 设置链接地址
              linkElement.target = '_blank'; // 在新标签页中打开链接

              const imgElement = document.createElement('img');
              imgElement.src = img;
              // imgElement.style.width = '50%';
              linkElement.appendChild(imgElement); // 将图片添加到链接标签中

              itemDiv.appendChild(linkElement); // 将链接标签添加到容器中

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

              // 将itemDiv添加到父容器中
              parentContainer.appendChild(itemDiv);

              outerDiv.appendChild(parentContainer);
            }
            console.log('请求成功');
          })
          .catch(error => {
            console.log('请求失败');
            console.log(error);
          });

      } else {
        console.log("没找到图片");
      }
    }
    // 输出结果
    console.log("content-script.js预加载完成。。");
  } else {
    console.log("没有找到元素。。");
  }
} catch (error) {
  // 处理错误的逻辑
  console.error("发生错误:", error);
}