def ffmpeginfo(self,stream_info:str="")	:
	"""
	description : this function is ffmpeg progess information decode
	--> Normal decode progess info "frame=  245 fps= 25 q=-1.0 size=    1297kB time=00:00:09.68 bitrate=1097.1kbits/s speed=1.01x" 
	--> Transcoding Progress info "frame=  189 fps= 20 q=14.0 size=    1262kB time=00:00:09.40 bitrate=1099.7kbits/s dup=30 drop=75 speed=0.98x"

	dup=30 drop=75
	"""
	keys=["frame","fps","size",'time','dup','drop','speed'] # Key word in ffmpeg progress information stream
	def func_time_decode(tmpstr):
		return datetime.datetime.strptime(tmpstr,'%H:%M:%S.%f').time()
	def func_others_decode(tmpstr):
		tmpvalue=None
		m = re.search(r'([-+]?[0-9]*\.?[0-9]*)',tmpstr)
		if m:
			tmpvalue=m.group()
		return tmpvalue

	func_mapping={"time":func_time_decode, \
				"frame":func_others_decode, \
				"fps":func_others_decode, \
				"size":func_others_decode, \
				"speed":func_others_decode, \
				}	
	ffmpeg_progressinfo={}
	tmp_value=""
	tmpres=[ item for item in stream_info.split(" ") if len(item)]
	if tmpres[0] not in "frame=": ## "frame=" is first key in ffmpeg progess information
		return ffmpeg_progressinfo
	tmpres.reverse()
	while tmpres:
		tmpstr=tmpres.pop()
		tmpsign=tmpstr[len(tmpstr)-1:]
		tmp_value=""
		if tmpsign in "=":
			tmp_value=tmpstr+tmpres.pop()
		else:
			tmp_value=tmpstr
		tmpkey=tmp_value.split("=")[0]
		tmpvalue=tmp_value.split("=")[1]
		if tmpkey in keys:
			infodecoder=func_mapping.get(tmpkey,func_others_decode)
			tmpvalue=infodecoder(tmpvalue)
			print("infodecoder",tmpkey,tmpvalue)
			ffmpeg_progressinfo[tmpkey]=tmpvalue
