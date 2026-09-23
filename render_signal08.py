from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W,H=1200,1500
BG="#07131f"; PANEL="#0d2030"; INK="#f5f7f2"; MUTED="#9db0ba"; CYAN="#4dd5d0"; LIME="#c7e34b"; GOLD="#f2b84b"; GRID="#254051"
out=Path(__file__).resolve().parent/"signal08_ai_power_linkedin.png"
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)

def font(size,bold=False):
    paths=["/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf","/System/Library/Fonts/SFNS.ttf"]
    for p in paths:
        try:return ImageFont.truetype(p,size)
        except:pass
    return ImageFont.load_default()
def text(x,y,s,size,color=INK,bold=False,anchor=None): d.text((x,y),s,font=font(size,bold),fill=color,anchor=anchor)
def box(x,y,w,h,r=20,fill=PANEL,outline=GRID,width=2): d.rounded_rectangle((x,y,x+w,y+h),r,fill=fill,outline=outline,width=width)

text(70,50,"GOKUL'S DATA SIGNAL 08",24,CYAN,True)
text(1130,53,"IEA • APR 2026",20,MUTED,True,"ra")
d.line((70,94,1130,94),fill=GRID,width=2)
text(70,135,"AI's next bottleneck",62,INK,True)
text(70,205,"isn't compute. It's power.",62,LIME,True)
text(70,292,"The executive question: can energy, grid access and resilience",25,MUTED)
text(70,328,"scale at the same speed as AI demand?",25,MUTED)

box(70,395,1060,250)
text(105,430,"GLOBAL DATA-CENTRE ELECTRICITY",19,MUTED,True)
text(105,486,"485",72,INK,True); text(280,528,"TWh",25,MUTED,True)
text(105,568,"2025",22,CYAN,True)
text(970,486,"950",72,INK,True,"ra"); text(1095,528,"TWh",25,MUTED,True,"ra")
text(1095,568,"2030",22,LIME,True,"ra")
x1,x2,y=350,815,535
d.line((x1,y,x2,y),fill=GRID,width=20)
d.line((x1,y,x2,y),fill=LIME,width=9)
d.polygon([(x2,y),(x2-27,y-17),(x2-27,y+17)],fill=LIME)
text(625,455,"+96%",54,LIME,True,"ma")
text(625,592,"14.4% compound annual growth",21,MUTED,False,"ma")

box(70,680,510,330)
text(105,715,"POWER DENSITY",18,CYAN,True)
text(105,755,"AI server racks are",28,INK,True)
text(105,792,"compressing the timeline.",28,INK,True)
vals=[("2020","1×",1),("2025","11×",11),("2027","44×",44)]
for i,(yr,lab,val) in enumerate(vals):
    yy=840+i*50; text(105,yy,yr,19,MUTED,True)
    d.rounded_rectangle((180,yy+2,490,yy+26),12,fill="#183447")
    width=max(10,int(310*val/44)); d.rounded_rectangle((180,yy+2,180+width,yy+26),12,fill=CYAN if i<2 else LIME)
    text(520,yy+1,lab,20,INK,True,"ra")
text(105,982,"2027 is a projection; index 2020 = 1.",13,MUTED)

box(620,680,510,330)
text(655,715,"WHERE THE GRID FEELS IT",18,GOLD,True)
text(655,755,"Share of electricity-demand",27,INK,True)
text(655,790,"growth driven by data centres",27,INK,True)
geo=[("Japan",">50%",52),("United States","~50%",50),("Malaysia","≤20%",20)]
for i,(name,lab,val) in enumerate(geo):
    yy=840+i*50; text(655,yy,name,18,MUTED,True)
    d.rounded_rectangle((805,yy+2,1045,yy+26),12,fill="#183447")
    d.rounded_rectangle((805,yy+2,805+int(240*val/60),yy+26),12,fill=GOLD)
    text(1095,yy+1,lab,20,INK,True,"ra")
text(655,982,"Contribution to national demand growth to 2030.",13,MUTED)

box(70,1045,1060,290,fill="#f1f1e7",outline="#f1f1e7")
text(105,1080,"THE DECISION SIGNAL",19,"#35505c",True)
text(105,1120,"Treat power as a product dependency.",40,"#07131f",True)
items=[("PLAN","Join AI demand forecasts to site and grid capacity."),("DESIGN","Model power, cooling and resilience before scale-up."),("GOVERN","Track utilisation and business value—not compute alone.")]
for i,(k,v) in enumerate(items):
    yy=1190+i*42; text(105,yy,k,16,"#087b82",True); text(205,yy,v,20,"#263c46")

d.line((70,1385,1130,1385),fill=GRID,width=2)
text(70,1410,"Source: IEA, Key Questions on Energy and AI • 16 Apr 2026",16,MUTED)
text(70,1440,"2025 values are estimates; 2030/2027 figures are projections.",16,MUTED)
text(1130,1434,"gokul-data.github.io/insights",18,CYAN,True,"ra")
im.save(out,quality=95)
print(out)
