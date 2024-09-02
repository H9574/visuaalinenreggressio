import capture_screenshots as capture
import collect_urls as collect
import compare_screenshots as compare
import time


### Define the URLs ###
old_url = 'https://www.punainenristi.fi'
new_url = 'https://www.punainenristi.fi'
###


def main():
    sitemap_url_old = old_url + '/sitemap.xml'
    sitemap_url_new = new_url + '/sitemap.xml'

    # Do collection of URLs
    collect.collect_url(sitemap_url_old, 'urls/old_sitemap.xml')
    collect.collect_url(sitemap_url_new, 'urls/new_sitemap.xml')

    # collect screenshots and compare them
    # Define the paths to the two XML files
    xml_file1 = 'urls/old_sitemap.xml'
    xml_file2 = 'urls/new_sitemap.xml'
    x = int(collect.number_of_urls(xml_file1))-1
    print("Alkuperäisten URLien määrä " + str(x))
    y = int(collect.number_of_urls(xml_file2))-1
    print("Uusien URLien määrä " + str(y))
    if(x == y):
        #continue to compare
        print('Starting to compare screenshots...')
        for number in range(x):
            #collect two screenshot at a time
            line1 = collect.get_url_lines(xml_file1, number)
            #line2 = collect.get_url_lines(xml_file2, number)
            line2 = new_url + collect.get_url_path(line1)
            #print(line2)
            #t0 = time.time()
            capture.capture_screenshot(line1, 'screenshots/original.png')
            capture.capture_screenshot(line2, 'screenshots/new_site.png')
            #t1 = time.time()
            #total = t1-t0
            #print(total)
            if compare.compare_screenshot('screenshots/original.png','screenshots/new_site.png') == True:
                #break
                continue
            else:
                #Save urls and pictures
                capture.screenshots_didnt_match('screenshots/original.png', f'failed/{number}/Should_be.png', f'failed/{number}/')
                capture.screenshots_didnt_match('screenshots/new_site.png', f'failed/{number}/Is.png', f'failed/{number}/')
                with open(f'failed/{number}/urls.txt', 'w') as file:
                    file.write(line1 + '\n' + line2)
                #break

    else:
        print('We are missing some URLs')

if __name__ == '__main__':
    main()
