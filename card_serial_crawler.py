from lxml import etree
import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}

url = 'https://playhearthstone.com/zh-tw/expansions-adventures/'
response = requests.get(headers=headers, url=url).text
tree_html = etree.HTML(response)
expansionList = tree_html.xpath('//div[@class="wrapper"]/div[2]/div/div/div/div')

i = 0
for expansionYear in expansionList:
    yearInfo_h3 = expansionYear.xpath('./div[1]/div[2]/h3/text()')[0]
    yearInfo_h5 = expansionYear.xpath('./div[1]/div[2]/div/h5/text()')[0]
    print(f'---------Year{i + 1}----------')
    yearIcon_src_list_4_8 = ['', '', '',
                             'https://d2q63o9r0h0ohi.cloudfront.net/images/icons/year/icon_year_dragon-253d1fb84d35f97e0a42e7b7d185056ec041bb15b3e4fc643bb641c06ea98ba4470be565c43f1a2ff191e37fc6319716c50f6955f76c49edce2e12f45c198319.png',
                             'https://d2q63o9r0h0ohi.cloudfront.net/images/icons/year/icon_year_raven-05890bd085f4256f4c1e99d31927ccf5823f8e0b2eb95691fbd41b62ccc2e42c22304c21918f3cdea087b5c25ca66249e806603ac1462a9a4a3f8ee9a8e5041b.png',
                             'https://d2q63o9r0h0ohi.cloudfront.net/images/icons/year/icon_year_mammoth-204d1eba168c2febf0a644d304fcf9982c220a167917f0fb94076c96e3a08d7bdee1688e9efabb8c6e0fd2592bf782d5244caea244ddb6b4e2698f0369da3566.png',
                             'https://d2q63o9r0h0ohi.cloudfront.net/images/icons/year/icon_year_kraken-94b80d5409c55c77a81998f8097b8a1ae6a7fb0f07838c486743ce366b87989f5efdda5012f2b45dac8b3bbf8a027910920fa0e3ff1d437e10dbf06cbee52716.png',
                             'https://d2q63o9r0h0ohi.cloudfront.net/images/icons/year/icon_year_classic-28bf7a259836fbe3d208cd192037e58e90dcac77de1561fe2a3e83c605ffbd981bd700ab4a9a8865b33d8232b6f4d859b42c348d168dd9c0925abf9a6c61aa89.png'
                             ]
    if i < 3:
        yearIcon_src = expansionYear.xpath('./div[1]/div[1]/img/@src')[0]
        # yearIcon_data = requests.get(url=yearIcon_src, headers=headers).content
        # icon = str(yearIcon_src).rsplit("/")
        # icon = icon[-1]
        # yearIcon_path = f'/yearly icons/{icon}'
        # with open(yearIcon_path, "wb") as iconStream:
        #     iconStream.write(yearIcon_data)
        context = (yearIcon_src, yearInfo_h3, yearInfo_h5)

    elif i == 3 or i == 7:
        yearIcon_src = yearIcon_src_list_4_8[i]
        context = (yearIcon_src, yearInfo_h3, yearInfo_h5)
    else:
        yearIcon_src = yearIcon_src_list_4_8[i]
        context = (yearIcon_src, yearInfo_h3, yearInfo_h5)

    slick_track = expansionYear.xpath('./div[2]/div')
    i0 = 1
    for slick_slide in slick_track:
        try:
            a_href = "https://playhearthstone.com" + slick_slide.xpath('./a/@href')[0]
            if i == 0 and (i0 == 2 or i0 == 3):
                logo_src = slick_slide.xpath('./a/div/div[1]/@style')[0]
                logo_src = str(logo_src).split("'")
                logo_src = logo_src[1]
                h4 = slick_slide.xpath('./a/div/div[3]/div/h4/text()')[0]
                h5 = slick_slide.xpath('./a/div/div[3]/div/h5/text()')[0]
                context = (a_href, logo_src, h4, h5)
            else:
                h4 = slick_slide.xpath('./a/div[1]/div[3]/div[2]/h4/text()')[0]
                h5 = slick_slide.xpath('./a/div[1]/div[3]/div[2]/h5/text()')[0]
                logo_src = slick_slide.xpath('./a/div[1]/div[3]/div[1]/img/@src')[0]
                if i == 1 or i == 2 or (i == 0 and i0 == 1):
                    background_src_0 = slick_slide.xpath('./a/div[1]/div/@style')[0]
                    background_src = str(background_src_0).split("'")
                    background_src = background_src[1]
                    # background_data = requests.get(url=background_src, headers=headers).content
                    # background_src = background_src.rsplit("/")
                    # background_name = background_src[-1]
                    # background_path = f'/background container/{background_name}'
                    # with open(background_path, "wb") as stream2:
                    #     stream2.write(background_data)
                    context = (a_href, background_src, logo_src, h4, h5)
                elif i == 3:
                    background_src_list = [
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/rise-of-shadows/tile-background-0afbbfa55914008793ccf6167448ed39cd1611889a28199144ae57d1c2310efe8b9aecace95894a10de18b8b762b4ee75fba80908a53cbca9752d2038f6578c2.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/saviors-of-uldum/tile-background-bfdef0c2ea8a1e3a4bd1d2c320e5ae7962dfc8fa74096ed9d627454606dcd450f334083d83134120635bd26110dd9c4daf6f563f4281a279b922001e6dd37368.jpg',
                        'https://images.blz-contentstack.com/v3/assets/bltc965041283bac56c/bltebbc800d9d98e71d/5e2eda9438960c7f6c000049/tile-background.jpg',
                        'https://images.blz-contentstack.com/v3/assets/bltc965041283bac56c/blt8e80f674b6c1874e/5e50545e297b4d1b5ff023a6/tile-background-2bec5f26774dcb00d1eedba461a03da0a60091f38756aa800755cdcebf9554764ca61e0854049fa30ecf2bc5506cb2a13cacf32dcd29ef28b14c1eab9884850b.jpg']
                    background_src = background_src_list[i0 - 1]
                    context = (a_href, background_src, logo_src, h4, h5)
                elif i == 4:
                    background_src_list = [
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/the-witchwood/tile-background-6202007b60513412e56aeba022e5c9c3a6c2ddbc20510f7b75b6662a81898d3b9028f0e0fa903f5bdbfae2fc3a30af4b0e9c387c83ef558ce660aa3bcc782583.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/the-boomsday-project/tile-background-cbf9e460956891e33569b2167b23b26af18ca5047e99dcdb16e138f645e519e94f1268aebad888cae4776b73410b7da4dfbfb4133702f717968d313120b268f3.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/rastakhans-rumble/tile-background-08711f129a6db833f65f68aae664dfbd09226822c525d6e3ca6efe06abae9549b7c7b3dfc500922818d8d31906c5e41dedaf736185e1a8d130f81826db81db63.jpg']
                    background_src = background_src_list[i0 - 1]
                    context = (a_href, background_src, logo_src, h4, h5)
                elif i == 5:
                    background_src_list = [
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/journey-to-ungoro/tile-background-c1aae2b5cd15d23e379bd511a69b48fcd452ab4678b03a66e2873d359e34c129b0b058ed096dac2c2db7419bf09d4849eddd67188b64ae990bfeb7ac6ae8dd4c.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/knights-of-the-frozen-throne/tile-background-0c028b60a086a83cc1b0e458e12b713dea8150162af4d919b7fbbd70931438ecc92ebcfde85701e72418ddcc20f09e5520e554d72ac4b6c3ddb57efda8921ba7.jpg',
                    'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/kobolds-and-catacombs/tile-background-51062802afb54589139edb5378eb404ce3f4261ad921db4d38230d7a9f8792bf445c11510be00f8f2e95ea5ede772ff090895eef7d885c94c0c7e9f4854883ac.jpg']
                    background_src = background_src_list[i0 - 1]
                    context = (a_href, background_src, logo_src, h4, h5)
                elif i == 6:
                    background_src_list = [
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/whispers-of-the-old-gods/tile-background-e5028f97f9f9a4cb885e8190082557d881c5eb57cf384dc4253bb047306fb62e04c550677124eb88a4bc41642da9f8e14df92a44a3c5dda1ff04dd736fd6021c.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/one-night-in-karazhan/tile-background-f2a970464e0d5c14aea408d935207d574dbaa62eb6a17518697e4f249c650e62d74f2625e39ebc9fba7c78ab1d95e7f9a2f5f70791d88614b429b18f156ba3f6.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/mean-streets-of-gadgetzan/tile-background-b572a3d7563b9f9a85dbd8877d26c864159ea6f7ceaf6ee60e761ccbbbffbc28f23c0d9d3eaf42cfe04a2b854c767ea4a91b3da825b63a48330b18c0178a02ac.jpg']
                    background_src = background_src_list[i0 - 1]
                    context = (a_href, background_src, logo_src, h4, h5)
                elif i == 7:
                    background_src_list = [
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/naxxramas/tile-background-4bc495498b64e90a2acefc157fb6a37d7da31ae32b758e3745f6f82a94e7fe3763d97de2c903dbbf5fd2de8247845e865b74481c416dcd62aabd438084f51a20.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/goblins-vs-gnomes/tile-background-fe6517dcaed861fe1fca6319cce686b374681e94dee414848984f0dd5697568993888cf06e672f0f27fc261f799bd379575357e8f92163b8ee816ab57153dda2.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/blackrock-mountain/tile-background-e7a9eee7ffd2757222afb295d9dc5316f8e2d7f9c1681e02fddf72b67a20462e6aa28ae72db23d927e584f2da61165ae71d67faf1cb44334477e87706680ddb2.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/the-grand-tournament/tile-background-52df10a9c314061717a02c49584575ed44cec1c3f5d4e6c3270def1f3542f1e6d3f5c83f64a18c27eabf2d61807264448b965fe9650b4897cbdb47873b6cdc40.jpg',
                        'https://d2q63o9r0h0ohi.cloudfront.net/images/card-sets/league-of-explorers/tile-background-f485ee94290d40c8a200f8d97c67ab643a3a3dad43c91ad0498890e610ed77c21ba84773a75e102132da1a6697246b90392f264ee648a50b74933836b7aad534.jpg']
                    background_src = background_src_list[i0 - 1]
                    context = (a_href, background_src, logo_src, h4, h5)

                # else:
                # background_src_0 = slick_slide.xpath('./a/div/div[1]/@class')[0]
                # background_src = str(background_src_0).split("'")
                # background_src = background_src[1]
                # background_data = requests.get(url=background_src, headers=headers).content
                # background_src = background_src.rsplit("/")
                # background_name = background_src[-1]
                # background_path = f'/background container/{background_name}'
                # with open(background_path2, "wb") as stream2:
                #     stream2.write(background_data)

                # logo_data = requests.get(url=logo_src, headers=headers).content
                # logo_name = slick_slide.xpath('./a/div[1]/div[3]/div/img/@alt')[0] + '.png'
                # logo_path = f'/logo container/{logo_src}'
                # with open(logo_path, "wb") as stream1:
                #     stream1.write(logo_data)
            i0 += 1
            print()
        except IndexError as e:
            print(e)
    i += 1
