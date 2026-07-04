各个模块分工：
	
	1. loader层：
	loader层主要是将文档转换成langchain document形式，用于存储到向量数据库
	2. embedding层：
	获取不同的embedding模型
	3. Vector strore层：
	获取不同的向量数据库，使用embedding模型将loader层转换的元数据向量化并存储到向量数据库中
	4. retriever层：
	用于创建不同的retriever，比如常见的vector Retriever、BM25、Hybrid Retriever、HyDE Retriever、Parent Retriever、RAG Fusion、Contextual Compression。Retriever层只做Retriever的创建
	5. llm层：
	获取不同的llm，比如deepseek、chatgpt
	6. agent层：
	agent层主要用于创建tool、agent和给llm的prompts，关系为tool中包含了不同的Retriever用于寻找数据，agent集合了llm、tool和对应的prompt
	7. splitter层：
	splitter层主要是用于切片操作，将loader层的文档使用embedding进行切片以供vectorstore使用。
	8. service层：
	service层分为两种，第一种是存储数据到向量数据库中，第二种是QA的功能。
	9. config层：
	config层用于存储配置文件，一些变量比如embedding类型、vector store类型可以写在配置文件中不用在代码中替换。
	10. controller层：
	controller层是程序入口，主要是用于调用service中的功能，可以接收用户的问题，提供llm的回复。
