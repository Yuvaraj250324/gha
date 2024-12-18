const core = require('@actions/core');
const exec = require('@actions/exec');

async function run() {
  try {
    const pythonVersion = core.getInput('python-version');
    await exec.exec(`python -m pip install --upgrade pip`);
    await exec.exec(`pip install -r requirements.txt`);
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();