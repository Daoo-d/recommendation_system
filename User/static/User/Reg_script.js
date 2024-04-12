const nextButton = document.querySelector('.btn-next');
const prevButton = document.querySelector('.btn-prev');
const steps = document.querySelectorAll('.step');
const form_steps = document.querySelectorAll('.form-step');
let active = 1;

nextButton.addEventListener('click', () => {
    active++;
    if(active > steps.length){
        active = steps.length;
    }
    updateProgress();
})

prevButton.addEventListener('click', () => {
    active--;
    if(active < 1){
        active = 1;
    }
    updateProgress();
})

const updateProgress = () => {
    console.log('steps.length =>' + steps.length);
    console.log('active =>' + active);

    steps.forEach((step,i) => {
        if(i == (active-1)){
            step.classList.add('active');
            form_steps[i].classList.add('active');
            console.log('i => '+ i);
        } else{
            step.classList.remove('active');
            form_steps[i].classList.remove('active');
        }
    });

    if(active === 1){
        prevButton.disabled = true;
    } else if(active === steps.length){
        nextButton.disabled = true;
        prevButton.disabled = false;
    } else {
        prevButton.disabled = false;
        nextButton.disabled = false;
    }
}
const skillsInput = document.getElementById('skillsInput');
const skillsContainer = document.getElementById('skillsContainer');

        // Listen for input changes
        skillsInput.addEventListener('input', updateSkills);

        function updateSkills() {
            const skills = skillsInput.value.trim();
            if (skills) {
                // Split skills by comma (you can adjust this based on your input format)
                const skillList = skills.split(',');

                // Clear existing skills
                skillsContainer.innerHTML = '';

                // Add each skill as a chip
                skillList.forEach(skill => {
                    const skillChip = document.createElement('div');
                    skillChip.classList.add('skill-chip');
                    skillChip.innerHTML = `
                        <span>${skill}</span>
                        <span class="cancel-icon" onclick="removeSkill(this)">❌</span>
                    `;
                    skillsContainer.appendChild(skillChip);
                });
            }
        }

        // Function to remove a skill
        function removeSkill(element) {
            const skillChip = element.closest('.skill-chip');
            skillChip.remove();
            skillsInput.value = "";
        }
