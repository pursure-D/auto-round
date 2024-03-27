git clone https://github.com/intel/auto-round
cd auto-round/examples/language-modeling
pip install -r requirements.txt
python3 main.py \
--model_name  google/gemma-2b \
--device 0 \
--group_size 128 \
--bits 4 \
--iters 400 \
--use_quant_input \
--deployment_device 'gpu' \
--output_dir "./tmp_autoround"