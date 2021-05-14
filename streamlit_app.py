import streamlit as st

st.write("输入示例：")
st.write(" 1．国网江苏电力：肖世杰董事长会见华为技术有限公司中国区电力总裁	2")
st.write("2．国网福建电力：谭永香董事长与中兴通讯公司举行会谈	2")
st.write("3．国网电动汽车：全生明董事长与中石化销售公司北京分公司总经理王顺江举行会谈	2")
st.write("4．国网上海电力：迅速传达学习贯彻辛保安董事长与上海市主要领导会谈精神和调研公司期间指示精神	2")
st.write("5．国网江苏电力：组织战略性新兴产业领导人员学习先进企业经验提升商业领导力	2 ")
st.title("参照以上样例文字将word目录复制到下面输入框中，并按Ctrl+Enter确定")
input = st.text_area("输入原始数据")
split_input = st.text_area("输入分隔符","■")
output = ""

input_format = input.replace(".",",").replace("．",",").replace(":",",").replace("：",",").replace("\t",",").replace(" ",",")

input_array = input_format.split("\n")
for i in range(len(input_array)):
    input_array[i] = input_array[i].split(",")

for i in range(len(input_array)):
    try:
         output = output + "__" + split_input + input_array[i][1] + "__" + input_array[i][2] +"。"
    except:
        pass

st.markdown(output)
st.title("复制以上文字到word并调整格式")
