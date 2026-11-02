// Mobile menu
const m=document.querySelector('.menu'),l=document.querySelector('.links');
if(m)m.addEventListener('click',()=>l.classList.toggle('open'));
document.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>l.classList.remove('open')));
// Scroll reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('show');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// Contact form -> email via FormSubmit (no backend needed)
const form=document.getElementById('projectForm');
if(form){
  const box=document.getElementById('formMsg'),btn=form.querySelector('button[type=submit]');
  form.addEventListener('submit',async e=>{
    e.preventDefault();
    if(form._honey.value)return;               // spam trap
    btn.disabled=true;btn.textContent='Sending…';box.className='msg';box.textContent='';
    try{
      const r=await fetch('https://formsubmit.co/ajax/tgnarayananmsc@gmail.com',{
        method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},
        body:JSON.stringify({
          name:form.name.value,email:form.email.value,phone:form.phone.value,
          project_type:form.type.value,budget:form.budget.value,timeline:form.timeline.value,
          requirements:form.requirements.value,
          _subject:'New project request from '+form.name.value,
          _replyto:form.email.value,_template:'table',_captcha:'false'})
      });
      const d=await r.json();
      if(r.ok&&(d.success===true||d.success==='true')){
        box.className='msg ok';box.textContent='✅ Thank you! Your request was sent. I will reply to your email soon.';form.reset();
      }else throw new Error(d.message||'Failed');
    }catch(err){
      box.className='msg err';box.textContent='❌ Could not send. Please email me directly at tgnarayananmsc@gmail.com';
    }
    btn.disabled=false;btn.textContent='Send project request ↗';
  });
}
// Project images: placeholder fallback + lightbox
document.querySelectorAll('.shot img').forEach(i=>{
  i.addEventListener('error',()=>i.parentElement.classList.add('empty'));
  if(i.complete&&i.naturalWidth===0)i.parentElement.classList.add('empty');
});
const lb=document.getElementById('lb');
if(lb){document.querySelectorAll('.shot').forEach(s=>s.addEventListener('click',()=>{
  const i=s.querySelector('img');if(s.classList.contains('empty'))return;
  lb.querySelector('img').src=i.src;lb.classList.add('on')}));
  lb.addEventListener('click',()=>lb.classList.remove('on'));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on')});}
